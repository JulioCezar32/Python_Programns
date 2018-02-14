import datetime as dt
import pandas as pd
import pymysql
import numpy as np

start = dt.datetime.now().time()
c = start.strftime('%H:%M:%S')
print
c + " Iniciado com Sucesso "

db_connection = pymysql.connect(
    host='meliuzrjmetrics.cput6rksaan1.sa-east-1.rds.amazonaws.com',
    db='mlz_rjm_cloudbi',
    user='user_google_apps',
    password='#eViu&9xcOpYRB327',
    charset='utf8')

df = pd.read_sql("""
SELECT 
    customer_id,
    DATE_FORMAT(MAX(affiliate_created_at),'%Y-%m-%d') AS ultima_compra,
    DATE_FORMAT(affiliate_created_at, '%Y%m') AS period,
    (CASE   WHEN me_parceiro.partner_type_id = 1 THEN 'ONLINE'
			WHEN (me_parceiro.partner_type_id = 2  AND transaction.partner_id != 2273) THEN 'POS'
			WHEN (transaction.partner_id = 2273 AND transaction.affiliate_created_at >='2017-03-13') THEN 'POS'
            WHEN (me_parceiro.partner_type_id = 3 OR (transaction.partner_id = 2273 AND transaction.affiliate_created_at <'2017-03-13')) THEN 'ERP'
            WHEN me_parceiro.partner_type_id = 4 THEN 'PARTNERSHIP'
	END
            ) AS business_unit
FROM transaction
JOIN me_parceiro ON me_parceiro.id = transaction.partner_id
WHERE transaction.kind IN ('sale', 'super_cashback', '100_percent')
GROUP BY customer_id, business_unit, period
UNION
SELECT 
    customer_id,
    DATE_FORMAT(MAX(affiliate_created_at),'%Y-%m-%d') AS ultima_compra,
    DATE_FORMAT(affiliate_created_at, '%Y%m') AS period,
    ('ALL') AS business_unit
FROM transaction
WHERE transaction.kind IN ('sale', 'super_cashback', '100_percent')
AND transaction.affiliate_created_at <= CURDATE()
GROUP BY customer_id, business_unit, period
ORDER BY business_unit, customer_id, period
""", con=db_connection)

end = dt.datetime.now().time()
c = end.strftime('%H:%M:%S')
print
c + "  Query executada com Sucesso "

df['period'] = df['period'].astype(int)
df_churned = df.copy()
if df.empty or df_churned.empty:
    exit(1)

df['id_diff'] = df['customer_id'] - df['customer_id'].shift(1)
df['month_diff'] = df['period'] - df['period'].shift(1)
df_churned['month_diff'] = df_churned['period'] - df_churned['period'].shift(-1)
df_churned['id_diff'] = df_churned['customer_id'] - df_churned['customer_id'].shift(-1)


def increase_1_month(row):
    if row['period'] % 100 == 12:
        return (row['period'] + 89)
    else:
        return (row['period'] + 1)


df_churned['period'] = df_churned.apply(increase_1_month, axis=1)


def calculate_mau_status(row):
    # If previous id is NaN, then is the first buy ever, consequently the first buy of the customer:
    if np.isnan(row['id_diff']):
        return 'NEW'
    # As the DataFrame is ordened by customer_id, when the previous ID is different (id_diff != 0) then is the first buy of customer:
    elif row['id_diff'] > 0:
        return 'NEW'
    else:
        # When (id_diff == 0) the next buy is from the same customer, having two option, be a retained buy(month_diff == 1)
        # or a resurrected(month_diff > 1)
        if (row['month_diff'] in [1, 89]):
            return 'RETAINED'
        else:
            return 'RESURRECTED'


def calculate_mau_status_churned(row):
    # for id_diff == 0 (same user), and month_diff not in -1(previous_month) or -88(previous_month, when the month is december)
    if (row['id_diff'] == 0) & (row['month_diff'] not in [-1, -89]):
        return 'CHURNED'
    # for id_diff < 0(other user), the previous id is churned
    elif row['id_diff'] < 0:
        return 'CHURNED'
    # for id_diff == NaN, the previous don't exist last register of user
    elif np.isnan(row['id_diff']):
        return 'CHURNED'
    else:
        # only a tag to filter in the next step
        return 'Outro'


start_time = dt.datetime.now().time()
c = start_time.strftime('%H:%M:%S')
print
c + "  1 etapa executada com Sucesso "

print
start_time

# Calculate churned status for channels based on previous functions
df_churned['mau_status'] = df_churned.apply(calculate_mau_status_churned, axis=1)
# Filters rows that are not churned
df_churned = df_churned[(df_churned['mau_status'] == 'CHURNED')]
df['mau_status'] = df.apply(calculate_mau_status, axis=1)
midle_time = dt.datetime.now().time()
c = midle_time.strftime('%H:%M:%S')
print
c + "  2 etapa executada com Sucesso "

df_final = pd.DataFrame()
df_final = pd.concat([df, df_churned])
month_limit = df_final['period'].max()
df_final = df_final[(df_final['period'] < (month_limit))]
df_final['period'] = df_final['period'].astype(str)
df_final['period'] = df_final['period'].apply(lambda x: '%s-%s-01' % (x[0:4], x[4:6]))

df_final.to_csv('mau_csv.csv')
end_time = dt.datetime.now().time()
print
end_time
print
"Executado com sucesso"

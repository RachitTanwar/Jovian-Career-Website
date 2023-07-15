from sqlalchemy import create_engine, text

db_connection = "mysql+pymysql://5oxiatp6bpxlh4b0m119:pscale_pw_90BbLUpHyOGlcln5G7lU2o2s3dO6KdYD3DSWJcUiNWk@aws.connect.psdb.cloud/joviancareers?charset=utf8mb4"
engine = create_engine(db_connection,connect_args={
    "ssl":{
        "ssl_ca": "/etc/ssl/cert.pem"
    }
})


with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    print(result.all())

result_dictionary = []
for row in result.all():
    result_dictionary.append(dict(row))

print(result_dictionary)
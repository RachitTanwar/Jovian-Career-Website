from sqlalchemy import create_engine, text

db_connection = "mysql+pymysql://5oxiatp6bpxlh4b0m119:pscale_pw_90BbLUpHyOGlcln5G7lU2o2s3dO6KdYD3DSWJcUiNWk@aws.connect.psdb.cloud/joviancareers?charset=utf8mb4"
engine = create_engine(db_connection,connect_args={
    "ssl":{
        "ssl_ca": "/etc/ssl/cert.pem"
    }
})



def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
            data = row._mapping
            jobs.append(data)
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(
      text(f"SELECT * FROM jobs WHERE id = :val"),
      {"val": id}
    )
    rows = result.mappings().all()
    if len(rows) == 0:
      return None
    else:
      return (dict(rows[0]))
    
def add_application_to_db(job_id, data):
    row = {
        "job_id": job_id,
        "full_name": data["full_name"],
        "email": data["emailid"],
        "linkedin_url": data["linkedin-url"],
        "education": data["education"],
        "work_experience": data["work_experience"],
        "resume_url": data["resume-url"],
    }
    with engine.connect() as conn:
        sql = text(
            "INSERT INTO applications(job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)"
        )
        conn.execute(sql, row)

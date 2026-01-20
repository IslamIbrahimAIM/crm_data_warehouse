from decouple import config

from pysparkJobs.base_spark_job import BaseSparkJob


class CreateReadOnlyUserJob(BaseSparkJob):

    APP_NAME = "Create Read Only DB User"

    def run(self):
        new_user = config("DASHBOARD", default="try harder")
        new_password = config("DASHBOARD_PASSWORD", default="keep trying")
        
        self.spark._jvm.org.apache.spark.sql.execution.datasources.jdbc.DriverRegistry.register(
            self.JDBC_DRIVER
        )        

        statements = [
            f"CREATE USER IF NOT EXISTS '{new_user}'@'%' IDENTIFIED BY '{new_password}'",
            f"GRANT SELECT ON washit_dw.gold_user_value_profile TO '{new_user}'@'%'",
            f"GRANT SELECT ON washit_dw.gold_dim_date TO '{new_user}'@'%'",
            "FLUSH PRIVILEGES"
        ]

        for sql in statements:
            self.execute_sql(sql)

    def stop(self):
        self.spark.stop()


if __name__ == "__main__":
    job = CreateReadOnlyUserJob()
    job.run()
    job.stop()

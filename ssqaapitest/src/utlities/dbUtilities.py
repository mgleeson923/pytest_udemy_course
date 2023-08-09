import pymysql
import logging as logger
from ssqaapitest.src.utlities.credentialsUtilities import CredentialUtility


class DBUtility(object):

    def __init__(self):
        creds_helper = CredentialUtility()
        self.creds = creds_helper.get_db_credentials()
        self.host = 'localhost'
        self.socket = "/Users/michaelgleeson/Library/Application Support/Local/run/E8ySqRq7C/mysql/mysqld.sock"

    def create_connection(self):
        connection = pymysql.connect(host=self.host, user=self.creds['DB_USER'], password=self.creds['DB_PASSWORD'],
                                     unix_socket=self.socket)
        return connection

    def execute_select(self, sql):
        conn = self.create_connection()

        try:
            logger.debug(f"Executing {sql}")
            cur = conn.cursor(pymysql.cursors.DictCursor)
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"Failed running SQL: {sql} \n Error: {str(e)}")
        finally:
            conn.close()

        return rs_dict

    def execute_sql(self, sql):
        pass

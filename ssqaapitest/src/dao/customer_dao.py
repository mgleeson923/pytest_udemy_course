from ssqaapitest.src.utlities.dbUtilities import DBUtility


class Customer_DAO(object):

    def __init__(self):
        self.db_helper = DBUtility()

    def get_customer_by_email(self, email):

        sql = f"SELECT * FROM local.wp_users WHERE user_email = '{email}';"
        rs_sql = self.db_helper.execute_select(sql)

        return rs_sql





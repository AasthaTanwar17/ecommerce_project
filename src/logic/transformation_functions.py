from pyspark.sql.functions import *

def standard_date(df, source_col, target_col):
    """
    It will standardize the mixed date string into DATE type and return null for the invalid dates.
    :param df: dataframe
    :param source_col: current date column
    :param target_col: new column name to store transformed dates
    """
    return df.withColumn(target_col, coalesce(
            try_to_date(trim(col(source_col)), "yyyy-MM-dd"),
            try_to_date(trim(col(source_col)), "yyyy/MM/dd"),
            try_to_date(trim(col(source_col)), "dd-MM-yyyy"),
            try_to_date(trim(col(source_col)), "MM/dd/yyyy"),
        )
                         )


# function to save dataframe into delta table
def save_df_to_delta(df, mode, path):
    return df.write.format("delta").mode(mode).saveAsTable(path)


# Function to capitalize string
def string_title_format(target_col):
    """
    This fucntion will return the transformed trimed string having first letter capitalized
    :param df: dataframe
    :param target_col: column needs to transform
    """
    return initcap(trim(col(target_col)))


def transformed_city(df, target_col):
    return df.filter((trim(col("city")) != "") &
                     (~lower(trim(col("city"))).isin("n/a", "na", "null")) & 
                      col("city").rlike("^[A-Za-z ]{2,}$"))
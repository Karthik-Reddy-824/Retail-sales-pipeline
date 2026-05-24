from scripts.extract import extract
from scripts.transform import transform
from scripts.load import load

def run():
    df = extract()
    orders, customers, products, regions = transform(df)
    load(orders, customers, products, regions)
    print(" ETL Pipeline Completed Successfully")

if __name__ == "__main__":
    run()
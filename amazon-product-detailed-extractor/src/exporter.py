import pandas as pd


def save_to_excel(all_products, product_name):
    df = pd.DataFrame(all_products)

    # Sorting by discounted price
    df["numeric_price"] = (
        df["discounted_price"]
        .str.replace("₹", "", regex=False)
        .str.replace(",", "", regex=False)
    )

    df["numeric_price"] = pd.to_numeric(df["numeric_price"], errors="coerce")

    df = df.sort_values(by="numeric_price")
    df = df.drop(columns=["numeric_price"])

    filename = f"{product_name}_products.xlsx"
    df.to_excel(filename, index=False)

    print(f"Excel saved successfully: {filename}")

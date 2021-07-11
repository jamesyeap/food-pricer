An API used for fetching the prices of food products from online supermarkets in Singapore (only supports NTUC at right now).

## Usage

Request method | API endpoint
--- | ---                                                 
`POST`| https://food-pricer.herokuapp.com/ntuc/

<details><summary>Sample input and output</summary>
  
#### Input 
```JSON
{
  "query" : "chicken breast"
}
  ```
#### Output (abbreviated for brevity)
```JSON
{
    "Aw's Market Chick Breast Fillet": {
        "link": "https://www.fairprice.com.sg/product/aw-s-market-chick-breast-fillet-300-g-90018535",
        "measurement": "300 G",
        "price": 3.61
    },
    "Aw's Market Chicken Breast Whole": {
        "link": "https://www.fairprice.com.sg/product/aw-s-market-chicken-breast-whole-400-g-90018633",
        "measurement": "400 G",
        "price": 5.0
    },
    "CP Raw Frozen Chicken Breast - Boneless Skin-on": {
        "link": "https://www.fairprice.com.sg/product/13049259",
        "measurement": "1kg",
        "price": 7.5
    },
    "CP Raw Frozen Chicken Breast - Skinless Boneless": {
        "link": "https://www.fairprice.com.sg/product/cp-raw-frozen-chicken-breast-skinless-boneless-1kg-13097998",
        "measurement": "1kg",
        "price": 8.25
    },
    "Chicken Story Fresh Black Pepper Chicken Boneless Breast": {
        "link": "https://www.fairprice.com.sg/product/chicken-story-fresh-black-pepper-chicken-boneless-breast-x-300g-90051017",
        "measurement": "- X 300G",
        "price": 4.5
    },
    "Chicken Story Fresh Chicken Boneless Breast": {
        "link": "https://www.fairprice.com.sg/product/chicken-story-fresh-chicken-boneless-breast-1-kg-90055862",
        "measurement": "1 KG",
        "price": 9.9
    },
}
```
</details>

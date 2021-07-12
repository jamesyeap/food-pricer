An API used for fetching the prices of food products from online supermarkets in Singapore (supports NTUC and Cold-Storage at the moment)

## Searching from NTUC

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
    "results": [
        {
            "link": "https://www.fairprice.com.sg/product/kee-song-boneless-breast-300g-13097675",
            "measurement": "300g",
            "price": 2.85,
            "supermarket": "ntuc",
            "title": "Kee Song Fresh Chicken - Boneless Breast"
        },      
        {
            "link": "https://www.fairprice.com.sg/product/aw-s-market-fresh-anxin-kampong-chicken-breast-450-g-90018526",
            "measurement": "450 G",
            "price": 4.56,
            "supermarket": "ntuc",
            "title": "Aw's Market Fresh Anxin Kampong Chicken Breast"
        },
        {
            "link": "https://www.fairprice.com.sg/product/13145817",
            "measurement": "300g",
            "price": 7.6,
            "supermarket": "ntuc",
            "title": "Kee Song Fresh Lacto Chicken - Boneless Breast"
        },
        {
            "link": "https://www.fairprice.com.sg/product/aw-s-market-duck-breast-fillet-400-g-90018553",
            "measurement": "400 G",
            "price": 9.31,
            "supermarket": "ntuc",
            "title": "Aw's Market Duck Breast Fillet"
        }
  ]
}
```
</details>

## Searching from Cold Storage

Request method | API endpoint
--- | ---                                                 
`POST`| https://food-pricer.herokuapp.com/cold-storage/

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
    "results": [
        {
            "link": "https://coldstorage.com.sg/fresh-s-l-chkn-breast-4-5034255",
            "measurement": "1PAK",
            "price": "7.35",
            "supermarket": "cold-storage",
            "title": "Skinless Chicken Breast 4 Pieces"
        },
        {
            "link": "https://coldstorage.com.sg/h-fresh-chicken-breast-2-5034252",
            "measurement": "1PAK",
            "price": "3.9",
            "supermarket": "cold-storage",
            "title": "Fresh Chicken Breast 2 Pieces"
        },
        {
            "link": "https://coldstorage.com.sg/fresh-chicken-breast-4-5034253",
            "measurement": "1PAK",
            "price": "7.35",
            "supermarket": "cold-storage",
            "title": "Fresh Chicken Breast 4 Pieces (With Skin)"
        }
  ]
}
```
</details>

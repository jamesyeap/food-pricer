An API used for fetching the prices of food products from online supermarkets in Singapore (supports NTUC and Cold-Storage at the moment)

## Searching from both NTUC and Cold-Storage

Request method | API endpoint
--- | ---                                                 
`POST`| https://food-pricer.herokuapp.com/

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
            "link": "https://coldstorage.com.sg/h-fresh-chicken-breast-2-5034252",
            "measurement": "1PAK",
            "price": "3.9",
            "supermarket": "cold-storage",
            "title": "Fresh Chicken Breast 2 Pieces"
        }
  ]
}
```
</details>

## Searching from NTUC only

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
        }
  ]
}
```
</details>

## Searching from Cold-Storage only

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
        }
  ]
}
```
</details>

# pizzafeed
#scraped Pizza coupons

This repository contain the codes used in scrapping coupons and offers off some pizza company's platform.
An api is created with two routes, one of it initializes a scrapping script data.py though there is a scheduler that runs the script every 30 mnutes, the second route fetches data in two methods i.e the POST and GET methods. The GET method fetches all coupons and offers data from the database while the POST method fetches the data based on a POST request body sent. The request body has to be in the format:

{
	"company":"company_name",
	"discountType":"COUPON/SALES & OFFERS",
	"page":"page_number"
}

The company names to be sent as request are listed below:

1. littleCeasars
2. papaJohns
3. dominos
4. pizzaHut
5. papaMurphys
6. marcosPizza

The discountType can either be :
1. COUPON
Or
2. SALES & OFFERS

Any other input different from these will result in errors.

The page number can either be empty or filled. If it is empty, the response gives all data for the particular pizza store and the discount type input but if the page number is filled, say 3, it gives data from the store and discount type on the page number where each page has 5 result. Therefore, if page number 3 is sent, it gives five data from the page 3. If there are no data on the page requested, an empty list will eb generated as a response to the request.

Though the page number may be empty, however the "page" key has to be part of the request body, this is how the API is structured.




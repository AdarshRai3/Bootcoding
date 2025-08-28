package main

func maximumProfit(prices []int)int{
	maxProfit:=int(^uint(0)>>1)
	minPrice:=0

	for _,price:= range prices{
		if minPrice>price{
			minPrice = price
		}

		if(maxProfit< price-minPrice){
			maxProfit = price-minPrice
		}
	}
	return maxProfit
}
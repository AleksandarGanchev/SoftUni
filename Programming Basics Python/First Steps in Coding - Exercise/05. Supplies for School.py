package_pens = int(input())
package_markers = int(input())
liqud = int(input())
percent_discount = int(input())


pens_price = package_pens * 5.80
markers_price = package_markers * 7.20
liquid_price = liqud * 1.20

total_price = pens_price + markers_price + liquid_price
discounted_price = total_price - (total_price * (percent_discount / 100))
print(discounted_price)
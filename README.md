# SwagLabs
QA automated test for https://www.saucedemo.com/

## Pages Included

- `HomePage`: Handles actions on the home page.
- `ProductsPage`: Handles actions on the products page.
- `CartPage`: Handles actions on the cart page.
- `CheckoutInformationPage`: Handles actions on the checkout information page.
- `CheckoutOverviewPage`: Handles actions on the checkout overview page.
- `CheckoutCompletePage`: Handles actions on the checkout complete page.

## Test Steps

1. Navigate to the Swag Labs home page.
2. Log in with standard user credentials.
3. Verify the disappearance of the login button on the products page.
4. Add two items ('Sauce Labs Fleece Jacket' and 'Sauce Labs Backpack') to the cart.
5. Click on the cart link.
6. Verify the disappearance of the products title on the cart page.
7. Verify the presence of the 'Your Cart' title on the cart page.
8. Check if both items are in the cart.
9. Proceed to checkout from the cart.
10. Fill out the checkout information form with name and zip code.
11. Continue to the checkout overview page.
12. Verify the presence of the 'Checkout: Overview' title on the overview page.
13. Check if both items are listed on the overview page.
14. Complete the purchase and verify the presence of the 'Checkout: Complete!' title.
15. Click on the menu icon, log out, and verify the login logo on the home page.

## Usage

1. Clone the repository.
2. Install required dependencies using `pip install -r requirements.txt`.
3. Download the appropriate WebDriver (e.g., ChromeDriver) and update the `driver_path` in the script.
4. Run the script:

```bash
python test_swag_labs.py
```

##Note

Make sure to update the WebDriver path and handle any changes in the Swag Labs website structure that might affect the script.

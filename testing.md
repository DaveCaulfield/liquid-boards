# Testing
- Testing was carried out throughout the development cycle. As each user story was completed acceptance criteria was checked.

- The deployed site was checked for appearance, responsiveness and funcionality to make sure it worked as expected for mobile, tablet, laptop and desktop devices and also for different browser types.



## Code Vaildation
- The code for Liquid Boards has been tested using [W3C HTML Validator](https://validator.w3.org/), [W3C CSS Validator](https://jigsaw.w3.org/css-validator/), [JS Hint](https://jshint.com//) and flake8 lint during development.


### Python validation
- Flake8 was used during development to catch any python code errors or warnings. Issues flaaged such as line too long or whitespace have been fixed. 
- There are lines of code created by Django with warning messages that have not been altered. 

### HTML Vaildation
![html validation](README/assets/html_validation.png)
- There were some minor fixes required after html validator testing found some missing/duplicate end tags.
- All html code writen has passed validation.

### CSS Vaildation
![css validation](README/assets/css_validation.png)
- CSS stylesheets were tested using [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and showed no errors.


### JS validation
![JS validation](README/assets/jshint.png)
- Javascript files were tested using [JS Hint](https://jshint.com//) and found an undefined variable for Stripe. This script is from Stripe and has been left as is.
- there is also a js script from mailchimp for the sites newsletter that showed up some warnings.




[EPIC 1: Viewing and navigation](https://github.com/DaveCaulfield/liquid-boards/issues/26)

[EPIC 2: Account Registration & Login](https://github.com/DaveCaulfield/liquid-boards/issues/27)

[EPIC 3: Search & Sort products ](https://github.com/DaveCaulfield/liquid-boards/issues/28)

[EPIC 4: Purchasing & Checkout](https://github.com/DaveCaulfield/liquid-boards/issues/29)

[EPIC 5: Site Administration](https://github.com/DaveCaulfield/liquid-boards/issues/30)

[EPIC 6: Engaging with the community](https://github.com/DaveCaulfield/liquid-boards/issues/32)







### Lighthouse

![Lighthouse](README/assets/lighthouse.png)

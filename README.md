## How to Run

1. Make sure you have the latest version of Python 3 installed.
2. `cd` into the project directory and run:

    `pip install -r requirements.txt`

    This will install all the required dependencies.
3. Make sure the Scrapy version is 2.0.0 or above. Run:
    
    `scrapy version`

    If it is below 2.0.0, then run:

    `pip install scrapy --upgrade`

4. Download geckodriver according to your OS from here: [https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases). And place the executable in a directory which is in your PATH. To test, run:

    `which geckodriver`

5. Now run the smartphones spider by:
    
    `scrapy crawl smartphones -o output/phones.jl`

    This will output the data in JSON Lines format.

## References & Tutorials Used

- https://docs.scrapy.org/en/latest/intro/tutorial.html
- https://docs.scrapy.org/en/latest/topics/dynamic-content.html
- https://github.com/clemfromspace/scrapy-selenium
- https://github.com/clemfromspace/scrapy-selenium/issues/42
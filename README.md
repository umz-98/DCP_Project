# Data collection pipeline project

## Milestone 1-2 - (Make sure to include your reasoning for choosing your website, the technologies you've used etc.)

- In this millstone a scraper class was created which includes the necessary methods to navigate the website such as: accept cookies and search. Furthermore, the scraper class also includes additional methods that could be of use e.g. scrolling the webpage and going to next webpage on a product list.

### Website

- The initial thought in selecting the website was to look at my personal interests. When shortlisting the websites, a list was created which included: JD sports, Netflix and PlayStation store. Out of them I was least engaged with the PlayStation store website since I haven’t been playing much lately. For that reason, I was left with JD and Netflix. I thought about the data that could be used to provide business value to them and had a much clearer image for JD. For that reason, I decided to go with this website. 

### Technologies

- Selenium allows for the control of web browsers, therefore was utilized to scrape the JD website. The information can be scraped using a code and interpreted with pandas making analysis much clearer. Below the code used to present data using pandas:

```python
"""pd.DataFrame()"""
```
## Milestone 3 (Talk about the methods you have added and the reasoning behind your approach.)

-Now that the navigation of the website was achieved through the previous milestone, the tasks in this milestone followed on.  Firstly, the ID of each product was located and its path was noted than the UUID library was used to generate UUID’s using the code below:
	
```python
"""uuid.uuid4()"""
```

### Dictionary and json_file

-Relevant details of the product were located and their xpaths were noted. Following this all the information was collected into a dictionary. Whilst not necessary pandas were used to visualize the dictionary for it to be more user-friendly.

-The dictionary created had to be saved in a json file, however the UUID had to be encoded to be saved. Therefore, the following final code was used to save the file:
	
```python
"""import json
from uuid import UUID

class UUIDEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return obj.hex
        return json.JSONEncoder.default(self, obj)
j = json.dumps(property_dict, cls=UUIDEncoder, indent=4)
f = open('data.json', 'w')
print(j, file=f)
f.close()"""
```

### Image links

-The URLIB library was implemented to download the images. However during the process a forbidden error was encountered therefore ‘headers’ were used which sorted out the problem. 

## Milestone 4

-In this milestone it was required to optimise and test the code written so far. The code was investigated for any nested loops or repeated codes.

### Docstrings

- Docstrings were added to each method using the following code (example shown):

```python
	    '''
        This method allows the 'accept cookies' button to be pressed
        
        parameters
        ----------
        xpath: str
            The xpath of locating the accept cookies button
        '''
```
- Docstrings give an explanation of the methods and can be called using 'help' unlike comments.
	
### unit tests

- All methods were tested using 'unit tests', this ensured the methods were running correctly. Below is one of the tests that were run:

```python
    def test_accept_cookies(self):
        expected_value = True
        actual_value= self.bot.accept_cookies(xpath = '//button[@class="btn btn-level1 accept-all-cookies"]')
        if actual_value == None:
            actual_value = True
        self.bot.driver.find_element(By.XPATH, '//a[@class="logo"]' )
        self.assertEqual(expected_value, actual_value)
```



	


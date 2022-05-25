# Data collection pipeline project

## Milestone 1-2 

- In this millstone a scraper class was created which includes the necessary methods to navigate the website such as: accept cookies and search. Furthermore, the scraper class also includes additional methods that could be of use e.g. scrolling the webpage and going to next webpage on a product list.

### Website

- The initial thought in selecting the website was to look at my personal interests. When shortlisting the websites, a list was created which included: JD sports, Netflix and PlayStation store. Out of them I was least engaged with the PlayStation store website since I haven’t been playing much lately. For that reason, I was left with JD and Netflix. I thought about the data that could be used to provide business value to them and had a much clearer image for JD. For that reason, I decided to go with this website. 

### Technologies

- Selenium allows for the control of web browsers, therefore was utilized to scrape the JD website. The information can be scraped using a code and interpreted with pandas making analysis much clearer. Below the code used to present data using pandas:

```python
"""pd.DataFrame()"""
```
## Milestone 3 

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

## Milestone 5

- In this milestone the scraped data was orderly stored and uploaded to RDS/S3.

### Raw data

- Raw data was uploaded to an S3 bucket that was created in AWS. The raw data included images and any json files. The data was uploaded using boto3 via the following code:

```python
import boto3
s3_client = boto3.client('s3')
response = s3_client.upload_file('/Users/FKhan/Downloads/miniconda3/DCP_Project/raw_data/Nike caps/Nike_Hat_15990063_355655.png', 'dcp1', 'Nike_Hat_15990063_355655.png')
```
- To upload multiple images at once a library named 'glob' was utilised.

```python
import glob
png_files = glob.glob('/Users/FKhan/Downloads/miniconda3/DCP_Project/raw_data/Nike caps/*.png')
```

### Tabular data

- The collected data was visualised as a table using pandas and uploaded to sql.

- A RDS database was created on AWS which was connected to VScode/sql using it's endpoint. The database was also connected to pgadmin for analysis purposes. Following this the tabular data was uploaded using 'sqalchemy' and 'psycopg2'. 

## Milestones 6 and 7

-To make the scraping more user friendly a code was added to avoid rescraping data. Below is an example where the scraper will avoid rescraping products with ID's that are present in the emperior armani (EA7) table.

```python
df = pd.read_sql('EA7_shoes', engine)
id_scraper = list(df['id'])
image_scraper = list(df['imagelinks_1'])
```

### Headless

- The scraper was run in headless mode where a few arguments were added at the initialisation step. The arguments that were added are shown below:
    
```python
options = Options()
options.add_argument('--user-agent=chrome:headless:userAgent=Mozilla/5.0 (X11\\; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36')
options.add_argument('--window-size=1920,1080')
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--no-sandbox")
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options=options
```

### Docker

- A dockerfile together with a txt file were created. These files would allow docker to run the scraper in an ec2 instance once a docker image has been built.
- The whole project repository was sent to the ec2 instance where a docker image was built this image was than run.

## Milestone 8

- The scraper was running how it's supposed to therefore in the following steps prometheus and grafana were setup.

### Prometheus

Prometheus is a software that allows for real-time monitoring of metrics and alerts.

- Initially a prometheus.yml file was set up to configure for prometheus where the host was set to 9090.

- The host connection was established by changing the security inbounds rules on the EC2 instance (including 9090) and than searching for EC2_ipaddress:9090

- To allow prometheus to monitor docker a docker job was added to the yaml file (code seen below) 

```python
  - job_name: 'docker'
        # metrics_path defaults to '/metrics' 
        # scheme defaults to 'http'
    static_configs:
      - targets: ['172.17.0.1:9323']
      # metrics added from our daemon.json file
```

- The deamon file was also edited by changing the ip address to 0.0.0.0 which would allow any connection.

- The docker connection was observed and the metrics were investigated

### Grafana

Grafana was utilized to allow the metrics to be visualized, hence to view the analytics of the scraping.

- Grafana was downloaded and connected in the terminal using the following commands:

'curl -O https://dl.grafana.com/enterprise/main/grafana-enterprise-9.0.0-1fcb2f45pre.darwin-amd64.tar.gz'
'tar -zxvf grafana-enterprise-9.0.0-1fcb2f45pre.darwin-amd64.tar.gz'
'./bin/grafana-server web'

- Grafana was connected to prometheus by adding a prometheus data source with the following URL: EC2_ipaddress:9090.

-Various metrics were visualized and a dashboard was created.






 

 

	


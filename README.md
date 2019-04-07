# got-script-scrapy

## Setup
1. clone and enter repo:
``` bash
git clone https://github.com/kaseyhackspace/got-script-scrapy
cd got-script-scrapy
```

2. Create `python3` virtual environment
``` bash
virtualenv -ppython3 env
```

3. Enter `virtualenv`:
``` bash
source env/bin/activate
```

## Running:

``` bash
scrapy crawl gottranscript -o <filename.json>
```
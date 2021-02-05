
# Wiki
A REST API to serve an encyclopedia like wikipedia.

## Demonstration
The demonstration of this API can be seen [here](https://wiki-rest-api.herokuapp.com/api/).

# Api Overview

**Show entries**
Returns all entries.

* **URL**

    /entries

* **Method:**
  

    GET

  
*  **URL Params**

    None

* **Data Params**

    None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** 
    {
        entries: ['bangladesh', 'computer', 'django', 'git', 'html', 'python', 'sass'],
    }


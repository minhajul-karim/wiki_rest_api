# Wiki
A REST API to serve an encyclopedia like wikipedia.

# Api Overview

**Show entries**
Returns all entries.

* **URL**

  <_/entries_>

* **Method:**
  
  <_GET_>
  
*  **URL Params**
None

* **Data Params**
None

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{
    "entries": [
        "bangladesh",
        "computer",
        "django",
        "git",
        "html",
        "python",
        "sass",
    ]
}`
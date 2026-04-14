# Shopify Interview
## Technical Challenge

### Setup
- Clone your repository to your local machine
  - `git clone git@github.com:ShopifyInterviews/technical-challenge-<firstname>-<lastname>.git`
- Create a new branch to complete the challenge:
  - `git checkout -b <challenge-name>`
- Write the code to complete the challenge in the language of your choice
- Commit your code that you've written
  - `git add .`
  - `git commit -m 'challenge complete'`
- Push your code to your repository
  - `git push -u origin <challenge-name>`

### Project 

#### URL Shortener

Create a URL shortening service, similar to http://bit.ly/ or other.

A user visiting your shortening website, which you can just run at `localhost:4567`, is prompted to enter the URL they wish to shorten. They are returned their new shortened URL which looks something like http://localhost:4567/a1b2c3. When visiting that URL they will be redirected to the original URL they submitted, or render a 404 if the URL does not exist.

The generated URL fragment should be short and unique.
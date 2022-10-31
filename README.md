# Syncave
Web app to easily collect and share information with others

## Motivation
* Learning FastAPI, Svelte and everything involved in developing and deploying a web app. 
* Having the ability to make my ideas a reality.

## Tech Stack
* JavaScript + Svelte in the frontend
* FastAPI (with Python) in the backend
* Supabase (Postgres) as the database
* Cypress and pytest for testing
* Deployed on Netlify and AWS EC2

## Timeline
* Sept 20 to 23, 2022: Started the project
* Sept 24, 2022: Created repository and upload on GitHub
* Oct 19, 2022: Added 'delete note' and 'create cave' functionality
* Oct 21, 2022: Added feedback button
* Oct 22, 2022: Implemented E2E tests
* Oct 23 to 26, 2022: 
  * Tried continuous integration with E2E and unit tests using Github Actions but wasn't succesful (see 'deployment' branch)
  * Wrote basic unit tests
* Oct 27 to 29, 2022:
  * Deployment of svelte app on Netlify
  * Dockerization and deployment of backend on a t2.micro AWS EC2 instance (Ubuntu)
  * Setting up custom domain for frontend (www.syncave.com) and backend ([api.syncave.com](api.syncave.com))
  * Tried setting up HTTPS for backend with certbot but wasn't successful yet
* Oct 30, 2022:
  * Improves color scheme in web app
  * Unified designs of buttons
  * Many small improvements in web app.



## Features
### Application
* Access space with (predefined) keys or directly through url
* Create notes and save in DB
* Load and display notes
* Notification toasts
* Basic UI
* Dark mode
* Delete note
* Create Cave
* Feedback button
### Deployment
* E2E tests
* Unit tests
* Svelte app deployed on netlify
* Dockerized backend
* FastAPI app deployed on a AWS t2.micro EC2 instance
* Custom domain for frontend and backend

## Next steps
* HTTPS for frontend and backend
* Fix E2E tests (some broke)
* Auto-deploy (CD) to Netlify and AWS on push
* Fixing bugs
### Potential further steps
* "Last used caves" on login screen
* Clean refreshing of notes after creating / deleting
* Redesign of UI
* Proper implementation of dark mode
* Info text for users
* Auto-testing (CI) on push
* encrypting data


### Discovered bugs
* Dark mode setting resetted when refreshing / redirecting page
* Page not accessible without 'www.'

## Screenshots
![](/docs/img/ss1.png)
![](/docs/img/ss2.png)
![](/docs/img/ss3.png)
![](/docs/img/ss4.png)
![](/docs/img/ss5.png)
![](/docs/img/ss6.png)


## E2E tests
https://user-images.githubusercontent.com/100248269/197353113-d547f76f-492b-4a07-977a-12eb0a3d1046.mp4



*updated: Oct 30, 2022*

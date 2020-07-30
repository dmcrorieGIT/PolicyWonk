# PolicyWonk
For HackTheNorth hackathon

![alt text](https://static.politico.com/dims4/default/d8adac8/2147483647/resize/1160x%3E/quality/90/?url=https%3A%2F%2Fstatic.politico.com%2F1f%2Fe5%2Fda07c20d4c04a878c2dbd661e54b%2F20191015-nancy-pelosi-gty-773.jpg)

## To Run Servers

### Backend
* From the root folder, go into the webserver folder: `cd webserver`
* Then, run `python3 manage.py runserver` to boot up your server
* Note: if you do not have python3 installed, you will want to do that
* That should be it! navigate to `http://127.0.0.1:8000/` to see your webrowser. Note that you will need to
go to a specific endpoint, the four set up at the time of this update are:
1. `http://127.0.0.1:8000/simulator_game/`
2. `http://127.0.0.1:8000/admin/`
3. `http://127.0.0.1:8000/api`
4. `http://127.0.0.1:8000/graphql/`

### Frontend (React)
* From the root folder, go into the frontend folder 
`cd frontend`
* Then, boot up react
`yarn start`
* Note: if you don't have yarn installed, you will want to do that

* And that's it! As you make changes to the `frontend/src/App.js`, they will automatically hot reload your localhost:3000 to reflect your changes

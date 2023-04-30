# Django CRUD Project

This is a simple Django web application that allows users to perform CRUD (Create, Read, Update, Delete) operations on data stored in a database. The application includes basic authentication and authorization features, as well as pagination .

## Getting Started

To get started with the project, you should first clone the repository:

```
git clone https://github.com/uishalcinha/django_project2_CRUD_operation.git
```

Next, create a virtual environment and install the required dependencies:

```
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Finally, run the development server:

```
python manage.py runserver
```

You should now be able to access the application by navigating to http://localhost:8000/ in your web browser.

## Usage

The application includes four main views, corresponding to the four CRUD operations:

- Create: `/create`
- Read: `/list`
- Update: `/update/<int:pk>`
- Delete: `/delete/<int:pk>`

The application also includes a search view at `/search`, which allows users to search for data based on specific criteria.

## Contributing

If you'd like to contribute to the project, you can submit a pull request with your changes. Please make sure to follow the existing coding style and include tests for any new features.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.


CREATE
![v1](https://user-images.githubusercontent.com/84958938/235328429-2a247f65-98c2-4f66-b8d4-fed55ffc773e.png)
DELETE
![v2](https://user-images.githubusercontent.com/84958938/235328431-ebfd6626-b7d5-4781-8737-6600fb0cf34c.png)
UPDATE
![v3](https://user-images.githubusercontent.com/84958938/235328432-0b961095-9514-44af-b1bf-026181048c14.png)
READ
![v5](https://user-images.githubusercontent.com/84958938/235328433-f78561fe-e8d5-45b4-9cb0-b5e1606a13ff.png)

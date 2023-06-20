## Q1. Notebook

Run this notebook for the February 2022 data.

What's the standard deviation of the predicted duration for this dataset?

* 5.672745068870966


## Q2. Preparing the output

What's the size of the output file?

* 48M

## Q3. Creating the scoring script

Now let's turn the notebook into a script. 

Which command you need to execute for that?

```bash
jupyter nbconvert --to script starter.ipynb
```

## Q4. Virtual environment

Now let's put everything into a virtual environment. We'll use pipenv for that.

Install all the required libraries. Pay attention to the Scikit-Learn version:
it should be `scikit-learn==1.2.2`. 

After installing the libraries, pipenv creates two files: `Pipfile`
and `Pipfile.lock`. The `Pipfile.lock` file keeps the hashes of the
dependencies we use for the virtual env.

What's the first hash for the Scikit-Learn dependency?

- `065e9673e24e0dc5113e2dd2b4ca30c9d8aa2fa90f4c0597241c93b63130d233`


## Q5. Parametrize the script

Let's now make the script configurable via CLI. We'll create two 
parameters: year and month.

Run the script for March 2022. 

What's the mean predicted duration? 

* 12.76

## Q6. Docker container 

Finally, we'll package the script in the docker container. 
For that, you'll need to use a base image that we prepared. 

Now run the script with docker. What's the mean predicted duration
for April 2022? 

```bash
$ docker build -t ride-duration-prediction-service:v1 .
$ docker run  ride-duration-prediction-service:v1 --year 2022 --month 4
12.827242870079969
```

* 12.83
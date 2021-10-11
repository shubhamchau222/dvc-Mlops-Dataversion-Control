# mlusecase(dvc) - (mlops)

In this project we'll see how we can use .dvc (data version control) in MLOP's

## wokflow -

<img src="https://github.com/shubhamchau222/dvc-MLusecase-mlops/blob/main/images/wrokflow.png" alt="workflow" width="70%">

## create fresh conda env
```bash 
        $ conda create -n dvc python=3.6 -y
        $ conda activate dvc 
        $ pip install -r requirements.txt 

```

## basic commands (commonly used command )
```bash 
        # git commands 
        $ git init
        $ git remote add origin <your repo link>
        $ git branch -M main
        $ touch README.md
        $ touch .gitignore
        $ git add .
        $ git commit -m 'basic setup added'
        $ git push -u origin main 
```
```bash 
        #  .dvc command
        $ pip install dvc 
        $ dvc init
        $ dvc repro 
        $ dvc dag

```


## dirs setup ( you can skip it )
```bash  
        # creating the packages  
        $ mkdir src      # source dir i
        $ mkdir utils               
        $ mkdir config     # dir to store config files 
        $ touch src/__init__.py          # for packaging 
        $ touch src/utils/__init__.py
        $ touch params.yaml 
        $ touch dvc.yaml 
        $ touch config/config.yaml    # yaml file for configurations


```

## creating the local dir as packages 

- create **src** dir as package 
- write setup.py file for that 

``` 
                # setup.py 

                from setuptools import find_packages, setup , find_packages 

                with open("README.md", "r", encoding="utf-8") as f:
                long_description = f.read()

                setup(
                name="src",
                version="0.0.1",
                author="shubhamchau222",
                description="A small package for dvc ml pipeline demo",
                long_description=long_description,
                long_description_content_type="text/markdown",
                url="https://github.com/shubhamchau222/dvc-MLusecase-mlops",
                author_email="shubhamchau78@gmail.com",
                packages=["src"],
                python_requires=">=3.6",
                install_requires=[
                        'dvc',
                        'pandas',
                        'scikit-learn'
                ]
                )
```
```bash 
    # to make src as a package
    # write package req in requirements.txt (install the local packages)
    # open requirement.txt  and write 
      $ -e . 

    here '.' means all local packages 

        $ pip install -r requirements.txt   # ( to install the local packages)

```

- **until tou install 'local packages' you'll get error 'src module' not found**



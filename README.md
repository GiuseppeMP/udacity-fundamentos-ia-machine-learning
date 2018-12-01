# How to create enviroment with conda

To create an environment:

>`conda create --name myenv`

Create the environment from the environment.yml file:

>`conda env create -f environment.yml`

To create an enviroment for the udacity class room:
>`conda create -n udacity-fundamentos-ia numpy jupyter notebook  pandas matplotlib seaborn python=3`

Activate & Deactivate enviroment

>`source activate udacity-fundamentos-ia`

>`source deactivate`

To list enviroments

>`conda env list`


# to run a jupyter notebook just run the code below on terminal or console:
>$`jupyter notebook`






# 01/dec/18 Repository Init


## Organização README.md


### fix CVE-2018-18074.
>More information
>moderate severity
>Vulnerable versions: <= 2.19.1
>Patched version: 2.20.0
>The Requests package through 2.19.1 before 2018-09-14 for Python sends an HTTP Authorization header to an http URI upon receiving a same-hostname https-to-http redirect, which makes it easier for remote attackers to >discover credentials by sniffing the network.

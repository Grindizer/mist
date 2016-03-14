## Mist
A command line tool that draw dependencies between micro services. 
For now can read service names and config from a deis cluster, ECS, k8s, to come. 

Typically, you have a deis cluster on which you deployed a set of application, 
that communicate in many ways. 
Since your applications fellow 12factor (http://12factor.net/) your applications contain indication about
other services through theit configuration (environment variable).

Mist read your application and theit configuration and try to guess 
which service reference which other one, and also check if your service use any 
kind of backing services (currently AWS elements supported: RDS, ElasticCache, SQS), and elasticsearch. 

(First version use endpoint names a lot, next version would check protocols when possible).

## Install

```
pip install git+https://github.com/Grindizer/mist.git
```

Or for a tagged version (1.0.3 for example.)

```
pip install git+https://github.com/Grindizer/mist.git@1.0.3
```

of from a cloned repo

```
git clone https://github.com/Grindizer/mist
cd mist
python setup.py install
```

Once installed you can run ::

```
mist --help
```

## Usage

```
Usage: mist [OPTIONS] COMMAND [ARGS]...

Options:
  --dont-show BOOLEAN
  --filename PATH
  --format [png|jpeg|pdf|svg]
  --engine [dot|fdp|neato]
  --help                       Show this message and exit.

Commands:
  deis
```

## Usage for deis clusters

```
Usage: mist deis [OPTIONS]

Options:
  -h, --endpoint TEXT  deis cluster endpoint  [required]
  -u, --username TEXT  deis user for login  [required]
  -p, --password TEXT  deis password  [required]
  --help               Show this message and exit.
```

## Development

To run the all tests run

```
py.test
```

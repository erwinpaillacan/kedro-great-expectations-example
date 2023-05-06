CONDA_ACTIVATE = source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate

install:
	conda create --name kedro-ge-example -y python=3.10
	$(CONDA_ACTIVATE) kedro-ge-example && \
	pip install -r src/requirements.txt

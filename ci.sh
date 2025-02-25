echo "==== black ===="
black .
echo "==== isort ===="
isort .
echo "==== pylint ===="
pylint avgmatrix
echo "==== mypy ===="
mypy avgmatrix
echo "==== pytest ===="
pytest --cov avgmatrix tests

# trivy-lab
Trivy LAB.

## Construir a imagem
`docker build -t vulnerable-app:1.0 .`

## Verificar se a imagem foi criada
`docker images | grep vulnerable-app`

## Scan básico
`trivy image vulnerable-app:1.0`

## Scan apenas vulnerabilidades HIGH e CRITICAL
`trivy image --severity HIGH,CRITICAL vulnerable-app:1.0`

## Scan com saída em formato JSON
`trivy image --format json --output results.json vulnerable-app:1.0`

## Scan com saída em formato de tabela
`trivy image --format table vulnerable-app:1.0`
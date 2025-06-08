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


## Apenas vulnerabilidades do OS
`trivy image --vuln-type os vulnerable-app:1.0`

## Apenas vulnerabilidades de bibliotecas
`trivy image --vuln-type library vulnerable-app:1.0`

## Scan de configuração (misconfigurations)
`trivy config Dockerfile`

## Scan de secrets
`trivy fs --security-checks secret .`


## Relatório detalhado em HTML
`trivy image --format template --template "@contrib/html.tpl" -o report.html vulnerable-app:1.0`

## Scan ignorando vulnerabilidades não corrigidas
`trivy image --ignore-unfixed vulnerable-app:1.0`

## Scan com timeout customizado
`trivy image --timeout 10m vulnerable-app:1.0`

---

## Run container
`docker run -d -p 5000:5000 --name vulnerable-app vulnerable-app:1.0`


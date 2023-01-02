**To avoid retyping too much info. Do a search and replace with your text editor for the following:**
`eos-xai`, `twitter_handle`, `project_title`, `project_description`

<!--
*** Forked by Best-README-Template by Othneil Drew.
-->

<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">Alla scoperta dell'eXplainable Artificial intelligence</h3>

  <p align="center">
    <br />
    <a href="https://github.com/anhelus/eos-xai"><strong>Documentazione</strong></a>
    <br />
    <br />
    <a href="https://github.com/anhelus/eos-xai/issues">Segnala un bug</a>
    ·
    <a href="https://github.com/anhelus/eos-xai/issues">Richiedi una nuova feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Contenuti</h2></summary>

  1. [Descrizione](#descrizione)
  2. [Librerie usate](#librerie-usate)
  3. [Per iniziare](#per-iniziare)
      * [Prerequisiti](#prerequisiti)
      * [Installazione](#installazione)
  4. [Utilizzo](#utilizzo)
  5. [Contribuire](#contribuire)
  6. [Licenza](#licenza)
  7. [Contatti](#contatti)

</details>

<!-- ABOUT THE PROJECT -->
## Descrizione

Questa è la repository di supporto per l'articolo di Elettronica Open Source "All’interno dell reti neurali con l’eXplainable Artificial Intelligence".

### Librerie usate

* [TensorFlow](https://www.tensorflow.org/)
* [Keras](https://keras.io/)
* [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/)

<!-- GETTING STARTED -->
## Per iniziare

Per iniziare, seguiamo questi passi.

### Prerequisiti

* pipenv
  ```sh
  pip install pipenv
  ```
  
### Installatione

1. Cloniamo la repository
   ```sh
   git clone https://github.com/anhelus/eos-xai.git
   ```
2. Installiamo i prerequisiti
   ```sh
   pipenv install
   ```
3. Testiamo lo script
   ```sh
   pipenv run python run.py -i imgs\\ball.jpg
   ```

## Usage

Lo script accetta due parametri:

* -i IMAGE, --image IMAGE: Percorso dell'immagine di input
* -t TITLE, --title TITLE: Titolo da visualizzare nell'immagine

<!-- CONTRIBUTING -->
## Contribuire

I contributi sono ciò che rendono la comunità open source quello che è, ovvero un posto incredibile dove imparare, ispirare, e creare. I vostri contributi sono quindi *enormemente* apprezzati. Per contribuire a questa repository:

1. Effettuate un fork del progetto.
2. Create il vostro Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Effettuate la commit delle vostre modifiche (`git commit -m 'Add some AmazingFeature'`).
4. Effettuate il push del vostro Feature Branch (`git push origin feature/AmazingFeature`).
5. Create una pull request.

<!-- LICENSE -->
## Licenza

Distribuito con [licenza MIT](LICENSE).

<!-- CONTACT -->
## Contatti

Angelo Cardellicchio - [mailto](mailto:a.cardellicchio@gmail.com)

Link al progetto: [https://github.com/anhelus/eos-xai](https://github.com/anhelus/eos-xai)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/anhelus/eos-xai.svg?style=for-the-badge
[contributors-url]: https://github.com/anhelus/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/anhelus/eos-xai.svg?style=for-the-badge
[forks-url]: https://github.com/anhelus/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/anhelus/eos-xai.svg?style=for-the-badge
[stars-url]: https://github.com/anhelus/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/anhelus/eos-xai.svg?style=for-the-badge
[issues-url]: https://github.com/anhelus/repo/issues
[license-shield]: https://img.shields.io/github/license/anhelus/eos-xai.svg?style=for-the-badge
[license-url]: https://github.com/anhelus/repo/blob/master/LICENSE.md
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/angelocardellicchio

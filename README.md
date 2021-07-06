# Rent4Events
[README po polsku](#-język-polski)
## <img src="https://static.vecteezy.com/system/resources/thumbnails/002/417/819/small_2x/illustration-of-the-united-kingdom-flag-free-vector.jpg" width=40px> English
🎉 Web app using Django and Vue.js for renting accessories for events ✏ 6th semester

Work in progress . . .

A web application supporting the event rental company (authorization, authentication, order management, CRUDs), working with Rest API.
Created with Vue.js & Django + using auth0 | 6th semester

App created by [@klaudial99]( https://github.com/klaudial99) and [@Kasden45]( https://github.com/Kasden45)

Web App is hosted on Heroku: https://rent4events.herokuapp.com/
<details>
  <summary>Click here to see the preview screenshots / Rozwiń aby zobaczyć pokazowe zdjęcia z aplikacji</summary>

  ![image](https://i.imgur.com/60iBZ7o.jpeg)*Home page / Strona główna*

  ![image](https://i.imgur.com/MzXlH9Z.jpeg)*Creating a new order / Tworzenie nowego zamówienia*

  ![image](https://i.imgur.com/KSgGIgs.jpeg)*Offer / Oferta*

  ![image](https://i.imgur.com/wjtMKN6.jpeg)*Order details / Szczegóły zamówienia*

  ![image](https://i.imgur.com/gUY8SDq.jpeg)*Confirm order modal / Modal potwierdzający zamówienie*

  ![image](https://i.imgur.com/cnCpofW.jpeg)*Courses / Kursy*

  ![image](https://i.imgur.com/6APIauO.jpeg)*Report example / Przykład raportu*

</details>


## Functionalities by role:
### Any user:
- Browsing company's offer
- Login
- Logout

### Guest (not logged in):
- Creating an account

### Client:
- Creating order
- Editing/cancelling his orders (if they haven't been already accepted by the manager)
- Browsing his orders

### Driver (Employee):
- Browsing his courses and editing their status (start or finish the course)
- Browsing orders and vehicles

### Manager:
- CRUD vehicles, products, employees, courses
- Applying courses to orders after accepting them
- Browsing, accepting, rejecting and commenting on orders
- Generating simple charts with company statistics

## Sample "login : password" pairs

### Clients:
- Klient1@example.com : Klient1! -> Zbigniew Nowakowski

### Drivers:
- Kierowca1@example.com : Kierowca1! -> Adam Nowak

- Kierowca2@example.com : Kierowca2! -> Jan Kowalski

- Kierowca3@example.com : Kierowca3! -> Albert Pięta


### Manager:
- kierownik@example.com : Kierownik1!



[README in English](#-english)

## <img src="https://upload.wikimedia.org/wikipedia/commons/7/7d/National_Flag_of_Poland.png" width=40px> Język Polski

🎉 Aplikacja webowa dla wypożyczalni eventowej napisana przy użyciu Django i Vue.js ✏ 6. semester

Praca w toku . . .

Aplikacja webowa wspomagająca funkcjonowanie wypożyczalni eventowej (autoryzacja, uwierzytelnianie użytkowników, zarządzanie zamówieniem, operacje CRUD),
korzystająca z Rest API.
Utworzona przy pomocy Vue.js & Django + korzystająca z auth0

Aplikacja zrealizowana przez [@klaudial99]( https://github.com/klaudial99) oraz [@Kasden45]( https://github.com/Kasden45)

Aplikacja została wdrożona w wersji pokazowej poprzez serwis Heroku: https://rent4events.herokuapp.com/
<details>
  <summary>Rozwiń aby zobaczyć pokazowe zdjęcia z aplikacji</summary>

  ![image](https://i.imgur.com/60iBZ7o.jpeg)*Strona główna*

  ![image](https://i.imgur.com/MzXlH9Z.jpeg)*Tworzenie nowego zamówienia*

  ![image](https://i.imgur.com/KSgGIgs.jpeg)*Oferta*

  ![image](https://i.imgur.com/wjtMKN6.jpeg)*Szczegóły zamówienia*

  ![image](https://i.imgur.com/gUY8SDq.jpeg)*Modal potwierdzający zamówienie*

  ![image](https://i.imgur.com/cnCpofW.jpeg)*Kursy*

  ![image](https://i.imgur.com/6APIauO.jpeg)*Przykład raportu*

</details>


## Funkcjonalność z podziałem na role użytkowników:
### Każdy użytkownik:
- Przeglądanie oferty wypożyczalni
- Logowanie
- Wylogowywanie

### Gość (niezalogowany):
- Tworzenie nowego konta

### Klient:
- Tworzenie zamówień
- Edytowanie/odwoływanie swoich zamówień (jeżeli nie zostały one wcześniej zaakceptowane przez kierownika)
- Przeglądanie swoich zamówień

### Kierowca (Pracownik):
- Przeglądanie swoich kursów i edytowanie ich statusu (rozpoczynanie lub zakańczanie kursów)
- Przeglądanie zamówień oraz pojazdów

### Kierownik:
- CRUD samochodów, asortymentu, pracowników, kursów
- Przydzielanie kursów do zaakceptowanych zamówień z opcją transportu
- Przeglądanie, akceptowanie, odrzucanie i komentowanie zamówień
- Generowanie prostych wykresów ze statystykami wypożyczalni

## Przykładowe pary "login : hasło"

### Klienci:
- Klient1@example.com : Klient1! -> Zbigniew Nowakowski

### Kierowcy:
- Kierowca1@example.com : Kierowca1! -> Adam Nowak

- Kierowca2@example.com : Kierowca2! -> Jan Kowalski

- Kierowca3@example.com : Kierowca3! -> Albert Pięta


### Kierownik:
- kierownik@example.com : Kierownik1!

## Att göta-lista - API
Jag har skapat ett API för att kunna hantera en att göra-lista med full CRUD-funktionalitet. Detta inkluderar funktionerna 
Create, Read, Update och Delete genom GET, POST, PUT, PATCH och DELETE.

### Anslutning till API
API:et är publicerat på Render och har URL:en: https://myapi-project-38vj.onrender.com.

### Tabeller i databasen

#### Tabell för inlägg
| Tabellnamn  | _id | title | description | status | 
| ------------- | ------------- | ------------- | ------------- | ------------- |
| todo  | SERIAL PRIMARY KEY  | STRING NOT NULL  | STRING  | STRING NOT NULL |

### Hur man använder API:et 
Det finns olika sätt att använda API:et för att nå det, nedan finns en tabell över vilka metoder som kan användas och vad de innebär. 

| Metod  | Ändpunkt | Beskrivning | 
| ------------- | ------------- | ------------- |
| GET | /api | Kopplar upp till API |
| GET  | /api/todo/  | Visar antal inlägg sparade i att göra-listan |
| POST  | /api/todo/  | Skapar ett ny inlägg med korrekt angett input |
| PATCH  | /api/todo/{id}  | Uppdatera delar av ett inlägg med angett id |
| PUT  | /api/todo/{id}  | Uppdatera hela inlägget med angett id |
| DELETE  | /api/todo/{id}  | Raderar ett inlägg med angett id |

#### Ett objekt som lägger till korrekt information om ett inlägg är uppbyggt så här:
```
{
  "title": "Titel",
  "description": "Beskrivning",
  "status": "Ej påbörjad"
}
```

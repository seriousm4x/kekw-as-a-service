FROM node:current-alpine as build

WORKDIR /usr/src/app

COPY kekw/package*.json ./

RUN npm ci --only=production

COPY kekw/ .

EXPOSE 8000

CMD ["node", "kekw.js", "--color=always"]

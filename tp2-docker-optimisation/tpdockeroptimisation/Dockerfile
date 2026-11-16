FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:20-alpine
WORKDIR /app
ENV NODE_ENV=development
COPY package*.json ./
RUN npm ci --omit=dev
COPY --from=build /app/server.js ./
EXPOSE 3000 4000 5000
USER root
CMD ["node", "server.js"]

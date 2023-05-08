FROM klakegg/hugo:0.107.0-ext-pandoc AS build

RUN apk add --update \
    wget

WORKDIR /site
COPY ./ /site

RUN apk add --no-cache \
    git && \
    git submodule update --init --recursive --depth 1


ARG HUGO_VERSION="0.107.0"

RUN hugo --minify --environment production -t hugo-book

FROM nginx:alpine
COPY --from=build /site/public /usr/share/nginx/html/

CMD ["/bin/sh", "-c", "exec nginx -g 'daemon off;'"]

EXPOSE 80
WORKDIR /usr/share/nginx/html

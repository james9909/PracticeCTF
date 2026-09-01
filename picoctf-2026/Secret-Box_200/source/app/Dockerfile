FROM node:18@sha256:5381bf8dd7e1dc53350b921f02811bd9167b34d3f7d0d8ebcc28229f65aef035 AS base

# Set up challenge directory
WORKDIR /challenge

# install packages
RUN npm install --no-package-lock \
	express \
	ejs \
	dotenv \
	pg \
	knex

# Copy only the source code
COPY src/ ./src/

# Specify a new stage for the challenge. Everything previous to this can be
# reused for every instance.
FROM base AS challenge
# Bring in FLAG from cmgr. Busts the cache every time.
ARG FLAG

# Open up this port for the web server
EXPOSE 80

CMD node /challenge/src/server.js



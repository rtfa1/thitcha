FROM node:20-bookworm-slim

# Create an unprivileged user for running Codex.
RUN useradd -m -u 10001 -s /bin/bash codex

# Install Codex CLI.
RUN npm install -g @openai/codex

# Install runtime utilities needed for device auth (curl + CA certs).
# Keep these installed as root, then switch to unprivileged `codex` user.
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
	&& apt-get install -y --no-install-recommends curl ca-certificates \
	&& rm -rf /var/lib/apt/lists/*

# Keep all work inside /workspace and avoid mounting other paths.
WORKDIR /workspace
VOLUME ["/workspace"]

USER codex

# Use Codex CLI as the entrypoint; pass args at `docker run`.
ENTRYPOINT ["codex"]

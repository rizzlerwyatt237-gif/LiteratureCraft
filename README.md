# Literature Craft

**A Minecraft survival adventure where the Literature Club helps build a home while real Juice Galaxy content begins leaking into the world.**

## What is in it

- **Minecraft: Java Edition** is the host game.
- **Doki Doki Literature Club!** is connected at runtime: the mod reads dialogue from the player's own DDLC installation.
- **Juice Galaxy** is connected at runtime: the mod locates the player's own installation and inspects its real files. The game files are never bundled in this repository.

## Current vertical slice

Install the mod in a Fabric 26.3 Minecraft instance and use:

- `/literaturecraft start` — starts the story and spawns Sayori, Natsuki, Yuri, and Monika as the first club settlement.
- `/literaturecraft ddlc` — checks for DDLC and reads a real dialogue line from its `.rpy` files.
- `/literaturecraft juice` — checks for Juice Galaxy and inventories its real install files.
- `/literaturecraft status` — prints the current mashup status.

This is **source-only / untested in a live game** until it has been built with Java 25 and launched in Minecraft 26.3.

## Build

The project targets Minecraft 26.3, Fabric Loader 0.19.5, Fabric Loom 1.17, and Java 25. Fabric's current 26.3 guidance specifies Loom 1.17, Gradle 9.6.0, and Loader 0.19.5.

```bash
./gradlew build
```

The built JAR will be under `build/libs/`.

## Important licensing rule

Do not add DDLC or Juice Galaxy game files, extracted assets, decompiled code, or other copyrighted game content to this repository. Literature Craft is designed to read the player's own installed copies at runtime.

## Roadmap

1. First club settlement vertical slice (current).
2. Real Juice Galaxy rift encounter driven by one detected asset/data entry.
3. Resource gathering and base-building objectives around the club.
4. Story progression tying DDLC dialogue to the rifts.
5. Real gameplay screenshot from the tested build.

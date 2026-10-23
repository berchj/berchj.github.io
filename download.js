// Fills the download buttons with the files of the latest GitHub release and
// suggests the one for the visitor's system. Without JS the links still go
// to the release page.
(async () => {
	const box = document.querySelector('[data-repo]');
	if (!box) {
		return;
	}

	const repo = box.dataset.repo;
	const FILES = {
		windows: {label: 'Download for Windows', match: /win-x64\.exe$/},
		macArm: {label: 'Download for Mac (Apple Silicon)', match: /mac-arm64\.dmg$/},
		macIntel: {label: 'Download for Mac (Intel)', match: /mac-x64\.dmg$/},
		appimage: {label: 'Download for Linux (AppImage)', match: /\.AppImage$/},
		deb: {label: 'Download for Ubuntu / Debian (.deb)', match: /\.deb$/},
	};

	const ua = navigator.userAgent;
	const system = /Windows/.test(ua) ? 'windows'
		: /Macintosh|Mac OS X/.test(ua) ? 'macArm'
			: /Ubuntu|Debian/i.test(ua) ? 'deb'
				: /Linux/.test(ua) ? 'appimage'
					: 'windows';

	try {
		const res = await fetch(`https://api.github.com/repos/${repo}/releases/latest`);
		if (!res.ok) {
			return;
		}

		const release = await res.json();
		const urls = {};
		for (const [key, {match}] of Object.entries(FILES)) {
			urls[key] = release.assets.find(a => match.test(a.name))?.browser_download_url;
		}

		const main = box.querySelector('.btn');
		if (urls[system]) {
			main.href = urls[system];
			main.querySelector('span').textContent = FILES[system].label;
		}

		box.querySelector('.others').replaceChildren(...Object.entries(FILES)
			.filter(([key]) => key !== system && urls[key])
			.map(([key, {label}]) => {
				const a = document.createElement('a');
				a.href = urls[key];
				a.textContent = label.replace('Download for ', '');
				return a;
			}));
		const version = box.querySelector('.version');
		if (version) {
			version.textContent = `Version ${release.tag_name.replace(/^v/, '')} · free · MIT license`;
		}
	} catch {} // offline or rate-limited: the plain links stay
})();

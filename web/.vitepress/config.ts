import { defineConfig } from "vitepress";

import graderItems from "./grader.g";

export default defineConfig({
  title: "Com Prog",
  description:
    "Website containing my solutions for Com Prog | เอาไว้โชว์เฉย ๆ ไม่ได้ให้ลอก",
  lastUpdated: true,
  outDir: "../dist",

  head: [
    [
      "link",
      {
        rel: "stylesheet",
        href: "https://fonts.googleapis.com/css?family=IBM+Plex+Sans+Thai",
      },
    ],
  ],

  themeConfig: {
    footer: {
      message: "Released under the MIT License",
      copyright: "Copyright © 2022 Nutthapat Pongtanyavichai",
    },
    socialLinks: [
      {
        icon: "github",
        link: "https://github.com/Leomotors/2110101-com-prog",
      },
    ],

    sidebar: [
      {
        collapsible: true,
        text: "Introduction",
        items: [
          {
            text: "Index",
            link: "/introduction/",
          },
        ],
      },
      {
        collapsible: true,
        text: "Grader Solutions",
        items: graderItems,
      },
    ],
  },
});

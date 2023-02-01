<div align="center">

## Serverless FrontEnd

</div>


This repo contains the code for frontend of CIFAR10 serverless inference ([link](https://frontend-next-js-ten.vercel.app/)). The frontend is built using [NEXT.JS](https://nextjs.org/). 

Next.js is an open-source web development framework created by Vercel enabling React-based web applications with server-side rendering and generating static websites. React documentation mentions Next.js among "Recommended Toolchains" advising it to developers as a solution when "Building a server-rendered website with Node.js". Where traditional React apps can only render their content in the client-side browser, Next.js extends this functionality to include applications rendered on the server-side. 

To get started with Next.js checkout this [link](https://beta.nextjs.org/docs/getting-started).

To deploy your Next.js app in vercel, check [this](https://vercel.com/guides/deploying-nextjs-with-vercel) and [this](https://vercel.com/blog/introducing-the-edge-runtime). 

One amazing thing with vercel deployments is that CI/CD pipelines are setup by default. This means that the pull requests are automatically deployed and you also get a preview before the actual deployment.


### How to run
To test the app locally run,

```bash
yarn create next-app --experimental-app
yarn dev
```
Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

With this, both [frontend](https://frontend-next-js-ten.vercel.app/) and [backend](https://github.com/gokul-pv/AWS-Lambda) can be deployed for free.
![](https://imgflip.com/s/meme/Leonardo-Dicaprio-Cheers.jpg)


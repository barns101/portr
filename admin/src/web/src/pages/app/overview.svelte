<script lang="ts">
  import Highlight from "svelte-highlight";
  import shell from "svelte-highlight/languages/shell";
  import yaml from "svelte-highlight/languages/yaml";
  import { toast } from "svelte-sonner";
  import "svelte-highlight/styles/stackoverflow-light.css";
  import { serverAddress, currentUser } from "$lib/store";
  import { onMount } from "svelte";

  const editConfigCommand = "portr config edit";
  const validateConfigCommand = "portr config validate";
  const helpCommand = "portr -h";

  let config: string;

  $: config = `
serverUrl: ${$serverAddress?.AdminUrl}
sshUrl: ${$serverAddress?.SshUrl}
secretKey: ${$currentUser?.secret_key}
tunnels:
  - name: portr
    subdomain: portr
    port: 4321
`.trim();

  const copyCodeToClipboard = (code: string) => {
    navigator.clipboard.writeText(code);
    toast.success("Code copied to clipboard");
  };

  const getServerAddress = async () => {
    const res = await fetch("/config/address");
    serverAddress.set(await res.json());
  };

  onMount(() => {
    getServerAddress();
  });
</script>

<p class="text-xl py-2">Client setup</p>

<div class="px-6 mt-2">
  <ul class="list-decimal space-y-4">
    <li>
      Download the portr client from <a
        href="/static/portr.zip"
        class="underline">here</a
      >
    </li>
    <li class="space-y-2">
      <span
        >Edit the portr client config file using the following command. This
        will open the default config file</span
      >
      <!-- svelte-ignore a11y-click-events-have-key-events -->
      <!-- svelte-ignore a11y-no-static-element-interactions -->
      <div
        class="border rounded-sm text-sm"
        on:click={() => copyCodeToClipboard(editConfigCommand)}
      >
        <Highlight language={shell} code={"$ " + editConfigCommand} />
      </div>
    </li>
    <li class="space-y-2">
      <span>Paste the following into the config file and save it.</span>
      <!-- svelte-ignore a11y-click-events-have-key-events -->
      <!-- svelte-ignore a11y-no-static-element-interactions -->
      <div
        class="border rounded-sm text-sm"
        on:click={() => copyCodeToClipboard(config)}
      >
        <Highlight language={yaml} code={config} />
      </div>
    </li>
    <li class="space-y-2">
      <span
        >Validate the config file by running the following command. This will
        validate the key and pull necessary credentials for the tunnel to work.
      </span>
      <!-- svelte-ignore a11y-click-events-have-key-events -->
      <!-- svelte-ignore a11y-no-static-element-interactions -->
      <div
        class="border rounded-sm text-sm"
        on:click={() => copyCodeToClipboard(validateConfigCommand)}
      >
        <Highlight language={shell} code={"$ " + validateConfigCommand} />
      </div>
    </li>
    <li>
      You're ready to use the tunnel, run <code
        class="border px-2 py-1 rounded-sm">{helpCommand}</code
      >
      or checkout the <a href="#" class="underline">cli docs</a> for more info.
    </li>
  </ul>
</div>
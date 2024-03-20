<script lang="ts">
  import { currentRequest } from "$lib/store";
  import { Button } from "$lib/components/ui/button";
  import { toast } from "svelte-sonner";
  import { RotateCw } from "lucide-svelte";

  const convertJsonToSingleValue = (data: any) => {
    const jsonKeyValue: any = {};
    for (const key in data) {
      jsonKeyValue[key] = data[key][0];
    }
    return jsonKeyValue;
  };

  let replaying = false;

  const replayRequest = async () => {
    replaying = true;

    try {
      const response = await fetch(
        `/api/tunnels/replay/${$currentRequest?.ID}`
      );
      if (!response.ok) {
        toast.error("Failed to replay request");
        return;
      }
      toast.success("Request replayed successfully");
    } catch (error) {
      toast.error("Failed to replay request");
    } finally {
      replaying = false;
    }
  };
</script>

<div class="flex-1 p-6 overflow-y-auto bg-white dark:bg-gray-800">
  <h2
    class="text-2xl font-semibold mb-4 text-gray-800 dark:text-gray-200 flex justify-between"
  >
    <div>
      {$currentRequest?.Method}
      <code class="font-light text-lg">{$currentRequest?.Url}</code>
    </div>
    <div>
      <Button disabled={replaying} on:click={replayRequest}>
        {#if replaying}
          <RotateCw class="mr-2 w-4 h-4 animate-spin" />
        {/if}
        Replay
      </Button>
    </div>
  </h2>
  <div class="space-y-6">
    <div>
      <h3 class="text-lg font-semibold text-gray-800 dark:text-gray-200">
        Request Headers
      </h3>
      <div class="rounded-md bg-gray-100 dark:bg-gray-700 p-4 mt-2">
        <pre
          class="text-sm font-mono text-gray-800 dark:text-gray-200 text-wrap break-words">{JSON.stringify(
            convertJsonToSingleValue($currentRequest?.Headers),
            null,
            2
          )}</pre>
      </div>
    </div>
    <div>
      <h3 class="text-lg font-semibold text-gray-800 dark:text-gray-200">
        Request Body
      </h3>
      <div class="rounded-md bg-gray-100 dark:bg-gray-700 p-4 mt-2">
        <pre
          class="text-sm font-mono text-gray-800 dark:text-gray-200">{$currentRequest?.Body}
        </pre>
      </div>
    </div>
    <div>
      <h3 class="text-lg font-semibold text-gray-800 dark:text-gray-200">
        Response Headers
      </h3>
      <div class="rounded-md bg-gray-100 dark:bg-gray-700 p-4 mt-2">
        <pre
          class="text-sm font-mono text-gray-800 dark:text-gray-200 text-wrap break-words">{JSON.stringify(
            convertJsonToSingleValue($currentRequest?.ResponseHeaders),
            null,
            2
          )}</pre>
      </div>
    </div>
    <div>
      <h3 class="text-lg font-semibold text-gray-800 dark:text-gray-200">
        Response Body
      </h3>
      <div class="rounded-md border p-4 mt-2">
        <!-- <pre
          class="text-sm font-mono text-gray-800 dark:text-gray-200">{byteArrayToText(
            $currentRequest?.ResponseBody
          )}</pre> -->
        <embed
          src="/api/tunnels/render/{$currentRequest?.ID}"
          width="100%"
          height="500px"
        />
      </div>
    </div>
  </div>
</div>
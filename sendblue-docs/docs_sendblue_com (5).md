[Skip to main content](https://docs.sendblue.com/docs/expressive-messages/#__docusaurus_skipToContent_fallback)

On this page

Expressve messages allow you to add an extra flare to the messages you send to iPhone users.

## Usage [​](https://docs.sendblue.com/docs/expressive-messages/\#usage "Direct link to Usage")

To send a message with a specific send style add the `send_style` field into the JSON body of the request so that your request looks like:

```codeBlockLines_e6Vv
{
  "number": "+19999999999",
  "content": "check it out - this message is invisible!",
  "send_style": "invisible"
}

```

### Possible values: [​](https://docs.sendblue.com/docs/expressive-messages/\#possible-values "Direct link to Possible values:")

| send\_style |
| --- |
| `"celebration"` |
| `"shooting_star"` |
| `"fireworks"` |
| `"lasers"` |
| `"love"` |
| `"confetti"` |
| `"balloons"` |
| `"spotlight"` |
| `"echo"` |
| `"invisible"` |
| `"gentle"` |
| `"loud"` |
| `"slam"` |

## Examples [​](https://docs.sendblue.com/docs/expressive-messages/\#examples "Direct link to Examples")

### Invisible ink: [​](https://docs.sendblue.com/docs/expressive-messages/\#invisible-ink "Direct link to Invisible ink:")

### Fireworks: [​](https://docs.sendblue.com/docs/expressive-messages/\#fireworks "Direct link to Fireworks:")

- [Usage](https://docs.sendblue.com/docs/expressive-messages/#usage)
  - [Possible values:](https://docs.sendblue.com/docs/expressive-messages/#possible-values)
- [Examples](https://docs.sendblue.com/docs/expressive-messages/#examples)
  - [Invisible ink:](https://docs.sendblue.com/docs/expressive-messages/#invisible-ink)
  - [Fireworks:](https://docs.sendblue.com/docs/expressive-messages/#fireworks)
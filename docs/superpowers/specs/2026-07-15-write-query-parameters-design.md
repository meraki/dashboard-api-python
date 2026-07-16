# Write-operation query parameters

## Problem

The generator documents query parameters on POST, PUT, and PATCH operations but only serializes request-body parameters. Those query parameters are silently dropped. Action-batch methods have the same omission because their action resource never receives a query string.

## Design

- Collect query parameters for every generated HTTP method.
- Pass both `params` and `json` through synchronous and asynchronous POST, PUT, and PATCH session helpers.
- For action batches, append encoded query parameters to the action `resource`, because the action format has no separate query-parameter field.
- Keep existing GET and DELETE behavior unchanged.
- Keep keyword validation aware of both query and body parameters.

## Test

Add one hermetic generator regression test using a synthetic POST operation with a boolean query parameter and a JSON body property. The test will verify that standard and asynchronous generated clients pass both `params` and `payload`, and that the batch client includes the encoded query parameter in its resource.

## Scope

No endpoint-specific exceptions, generated API regeneration, new dependency, or unrelated refactoring is included.

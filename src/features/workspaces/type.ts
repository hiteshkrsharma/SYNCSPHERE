import { Models } from "node-appwrite";
import { string } from "zod";

export type Workspace = Models.Document & {
    name: string;
    imageUrl: string;
    inviteCode: string;
    userId: string;
}; 
 